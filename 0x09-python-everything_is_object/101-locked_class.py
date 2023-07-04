class LockedClass:
    def __setattr__(self, name, value):
        if hasattr(self, name) and name != 'first_name':
            raise AttributeError("'LockedClass' object cannot create new attributes")
        super().__setattr__(name, value)

