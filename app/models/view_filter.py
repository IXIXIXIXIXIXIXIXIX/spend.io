class ViewFilter:

    def __init__(self):

        self.visible_tags = []
        self.visible_merchants = []
        self.filter_active = False

    def add_tag(self, tag):

        if tag not in self.visible_tags:
            self.visible_tags.append(tag)
            self.filter_active = True
        
    def remove_tag(self, tag):

        if tag in self.visible_tags:
            self.visible_tags.remove(tag)
            
            if len(self.visible_tags) == 0 and len(self.visible_merchants) == 0:
                self.filter_active = False

    def add_merchant(self, merchant):

        if merchant not in self.visible_merchants:
            self.visible_merchants.append(merchant)
            self.filter_active = True
        
    def remove_merchant(self, merchant):

        if merchant in self.visible_merchants:
            self.visible_merchants.remove(merchant)
            
            if len(self.visible_merchants) == 0 and len(self.visible_tags) == 0:
                self.filter_active = False


    def activate_filter(self):
        
        if len(self.visible_tags) > 0 or len(self.visible_merchants) > 0:
            self.filter_active = True

    def deactivate_filter(self):

        self.filter_active = False