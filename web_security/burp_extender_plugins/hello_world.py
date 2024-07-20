from burp import IBurpExtender  # required for all extensions to work

class BurpExtender(IBurpExtender):
    
    def registerExtenderCallbacks(self, callbacks):
        
        # keep a reference to our callbacks object
        self._callbacks = callbacks
        
        # set our extension name
        callbacks.setExtensionName("From Null Class")
        
        print("Hello Null folks!")
        
        return 
