class Logger:
    def __init__(self):
        pass
    
    @staticmethod
    def success(msg):
        msg = "{} {}".format("✅ ",msg)
        print(msg)
    
    @staticmethod
    def info(msg):
        msg = "{} {}".format("ℹ️ ",msg)
        print(msg)
    
    @staticmethod
    def warning(msg):
        msg = "{} {}".format("⚠️  ",msg)
        print(msg)
    
    @staticmethod
    def error(msg):
        msg = "{} {}".format("🛑 ",msg)
        print(msg)