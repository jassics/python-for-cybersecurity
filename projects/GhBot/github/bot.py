from pydantic import ConfigError
from github.loggers import Logger
from github.config import GhConfig
import requests as req
from bs4 import BeautifulSoup
import json
import os

class GhBot:
    def __init__(self):
        self.page_exists = None
        self.data_dict = {}
        self.soup = None
        self.followers = []
        self.following = []
        self.notFollowingBack = []
        self.unfollowed = []
        self.userUnfollowed = []
        self.recentFollowers = []
        self.recentUnfollowers = []
        self.recentlyFollowedByUser = []
        self.recentlyUnfollowedByUser = []
    

    def getUserInput(self):
        Logger.info("1. Run for default username ({})".format(GhConfig.DefaultProfile.USERNAME))
        Logger.info("2. Run for another username")
        menu = input("Your Choice: ")

        if menu == "1":
            self.username = GhConfig.DefaultProfile.USERNAME

        elif menu == "2":
            self.username = input("Enter username: ")

        else:
            Logger.error("Oops, wrong input. Exiting program")
    

    def createSoupURL(self,tab_name,currPg):
        return f"https://github.com/{self.username}?tab={tab_name}&page={currPg}"
    
    def checkUserExists(self):
        url=f"https://github.com/{self.username}"
        status = self.getSoup(url)
        if status is not None:
            return True
        else:
            return False

    def getSoup(self,url):
        try:
            response = req.get(url)

            if str(response.status_code) == '404':
                Logger.error("Page Not Found. Error 404")
                return None
            else:
                html = response.content
                soup = BeautifulSoup(html,'html.parser')
                return soup

        except Exception as e:
            Logger.error(e)
            return None
    


    def getData(self,tab_name):
        currPg = 1
        prev_len = curr_len = 0
        
        while(True):
            try:
                url = self.createSoupURL(tab_name=tab_name,currPg=currPg)
                self.soup = self.getSoup(url=url)

                if self.soup is None:
                    return None
                
                tab_list = self.soup.find_all(GhConfig.CSS.OUTER_ELM, class_=GhConfig.CSS.OUTER_CLASS)

                if tab_name == "followers":
                    prev_len = len(self.followers)

                    for element in tab_list:
                        data  = element.find_all(GhConfig.CSS.INNER_ELM, class_=GhConfig.CSS.INNER_CLASS)
                        self.followers.append(data[0].string)
                
                    curr_len = len(self.followers)
                    currPg+=1

                    if prev_len == curr_len:
                        return self.followers

                elif tab_name == "following":
                    prev_len = len(self.following)

                    for element in tab_list:
                        data  = element.find_all(GhConfig.CSS.INNER_ELM, class_=GhConfig.CSS.INNER_CLASS)
                        self.following.append(data[0].string)
                    
                    curr_len = len(self.following)
                    currPg+=1

                    if prev_len == curr_len:
                        return self.following

                
            except Exception as e:
                Logger.error(e)
                return None
    

    def getUserNotFollowingBack(self):
        follower_set = set(self.followers)
        following_set = set(self.following)
        self.userNotFollowingBack = list(follower_set - following_set)
        return self.userNotFollowingBack


    def getRecentFollowers(self):
        prev_followers_set =  set(self.prevProfile["all_followers"])
        curr_followers_set = set(self.followers)
        recentFollowers = list(curr_followers_set-prev_followers_set)
        return recentFollowers

    def getRecentUnfollowers(self):
        prev_follower_set =  set(self.prevProfile["all_followers"])
        curr_follower_set = set(self.followers)
        recentUnfollowers = list(prev_follower_set-curr_follower_set)
        return recentUnfollowers


    def getRecentlyFollowedByUser(self):
        prev_following_set = set(self.prevProfile["all_following"])
        curr_following_set = set(self.following)
        recentlyFollowedByUser = list(curr_following_set - prev_following_set)
        return recentlyFollowedByUser
        

    def getRecentlyUnfollowedByUser(self):
        prev_following_set =  set(self.prevProfile["all_following"])
        curr_following_set = set(self.following)
        recentlyUnfollowedByUser = list(prev_following_set - curr_following_set)
        return recentlyUnfollowedByUser

    def getSavedProfileData(self):
        filename = f"profile-{self.username}.json"
        filePath = GhConfig.buildPATH(GhConfig.IO.OUTPUT,filename)
        if os.path.isfile(filePath):
            with open(filePath,"r") as f:
                profile_dict = json.load(f)
            f.close()
            return profile_dict
        else:
            return None



    def serve(self,content:str):
        try:
            if len(content)==0:
                status="error"
                msg="username null exception"
                return self.data_dict,status,msg

            self.username = content

            if not self.checkUserExists():
                status="error"
                msg="User not found"
                Logger.error(msg)
                return self.data_dict,status,msg
            else:
                Logger.success(f"Found profile for {self.username}")


            followers = self.getData(tab_name="followers")
            following = self.getData(tab_name="following")
            
            if followers is None or following is None:
                status="error"
                msg="failed to establish connection"
                return self.data_dict,status,msg
            

            self.prevProfile = self.getSavedProfileData()
            self.data_dict = {
                                "username": self.username,
                                "followers":0,
                                "following":0,
                                "recently_followed":[],
                                "recently_unfollowed":[],
                                "recently_followed_by_user":[],
                                "recently_unfollowed_by_user":[],
                                "all_followers":[],
                                "all_following":[]
                            }

            follower_count = len(followers)
            following_count = len(following)

            # set the followers and following count in dict
            self.data_dict["followers"] = follower_count
            self.data_dict["following"] = following_count

            # Set the a;l-followers and all-following in dict
            self.data_dict["all_followers"] = followers
            self.data_dict["all_following"] = following

            # If the profile exists previously
            if self.prevProfile is not None:
                self.data_dict["recently_followed"] = self.getRecentFollowers()
                self.data_dict["recently_unfollowed"] = self.getRecentUnfollowers()
                self.data_dict["recently_followed_by_user"] = self.getRecentlyFollowedByUser()
                self.data_dict["recently_unfollowed_by_user"] = self.getRecentlyUnfollowedByUser()
                self.save(status="updated")
                
                status = "success"
                msg="updated profile"
                return self.data_dict,status,msg
            else:
                # else create profile
                self.save()
                status = "success"
                msg="created profile"
                return self.data_dict,status,msg

        except Exception as e:
            status = "error"
            msg=f"{e}"
            return self.data_dict,status,msg
        

    def save(self,status=""):
        filename = f"profile-{self.username}.json"
        filePath = GhConfig.buildPATH(GhConfig.IO.OUTPUT,filename)
        with open(filePath,"w") as f:
            json.dump(self.data_dict,f,indent=6)
        f.close()

        if status=="updated":
            Logger.success(f"Profile data for username {self.username} have been updated and saved to path: {filePath}")
        else:
            Logger.success(f"Profile data for username {self.username} created and saved to path: {filePath}")