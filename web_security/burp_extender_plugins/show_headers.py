from burp import IBurpExtender               # Required for all extensions
from burp import IMessageEditorTab           # Used to create custom tabs within the Burp HTTP message editors
from burp import IMessageEditorTabFactory    # Provides rendering or editing of HTTP messages, within within the created tab
from burp import IHttpListener               # This method is invoked when an HTTP request is about to be issued, and when an HTTP response has been received.
from exceptions_fix import FixBurpExceptions # Used to make the error messages easier to debug
import sys                                   # Used to write exceptions for exceptions_fix.py debugging

class BurpExtender(IBurpExtender, IMessageEditorTabFactory):
    ''' Implements IBurpExtender for hook into burp and inherit base classes.
        Implement IMessageEditorTabFactory to access createNewInstance.
    '''
    def registerExtenderCallbacks(self, callbacks):

        # required for debugger: https://github.com/securityMB/burp-exceptions
        sys.stdout = callbacks.getStdout()

        # keep a reference to our callbacks object
        self._callbacks = callbacks

        # obtain an extension helpers object
        # This method is used to obtain an IExtensionHelpers object, which can be used by the extension to perform numerous useful tasks
        self._helpers = callbacks.getHelpers()

        # set our extension name
        callbacks.setExtensionName("Security Headers")

        # register ourselves as a message editor tab factory
        callbacks.registerMessageEditorTabFactory(self)
        
        print("All is well. Check your custom tab")

        return
        
    def createNewInstance(self, controller, editable):
        ''' Allows us to create a tab in the http tabs. Returns 
        an instance of a class that implements the iMessageEditorTab class
        '''
        return DisplayValues(self, controller, editable)
        

class DisplayValues(IMessageEditorTab):
    ''' Creates a message tab, and controls the logic of which portion
    of the HTTP message is processed.
    '''
    def __init__(self, extender, controller, editable):
        ''' Extender is a instance of IBurpExtender class.
        Controller is a instance of the IMessageController class.
        Editable is boolean value which determines if the text editor is editable.
        '''
        self._txtInput = extender._callbacks.createTextEditor()
        self._extender = extender

    def getUiComponent(self):
        ''' Must be invoked before the editor displays the new HTTP message,
        so that the custom tab can indicate whether it should be enabled for
        that message.
        '''
        return self._txtInput.getComponent()
    
    def getTabCaption(self):
        ''' Returns the name of the custom tab
        '''
        return "Security Response Headers"
        
    def isEnabled(self, content, isRequest):
        ''' Determines whether a tab shows up on an HTTP message
        '''
        if isRequest == True:
            requestInfo = self._extender._helpers.analyzeRequest(content)
            headers = requestInfo.getHeaders();
            headers = [header for header in headers]
            self._headers = '\n'.join(headers)
        return isRequest and self._headers
        
    def setMessage(self, content, isRequest):
        ''' Shows the message in the tab if not none
        '''
        if (content is None):
            self._txtInput.setText(None)
            self._txtInput.setEditable(False)
        else:
            self._txtInput.setText(self._headers)
        return
        
FixBurpExceptions()
