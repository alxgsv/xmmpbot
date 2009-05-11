class PresenceStorage(object):
    pass

class MemoryPresenceStorage(PresenceStorage):
    user_presences = {}
    
    def set_presence(self, who, show, status):
        self.user_presences[who.getStripped()] = [show, status]
        
    def get_presence(self, who):
        return self.user_presences[who.getStripped()]
    
    def __str__(self):
        return self.user_presences.__str__()