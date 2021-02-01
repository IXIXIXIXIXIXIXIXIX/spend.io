class ViewFilter:

    def __init__(self):

        self.tag_ids = []
        self.merchant_ids = []
        self.filter_active = False

    def add_tag(self, tag):

        if tag.id not in self.tag_ids:
            self.tag_ids.append(tag.id)
            self.filter_active = True
        
    def remove_tag(self, tag):

        if tag.id in self.tag_ids:
            self.tag_ids.remove(tag.id)
            if len(self.tag_ids) == 0 and len(self.merchant_ids) == 0:
                self.filter_active = False

    def add_merchant(self, merchant):

        if merchant.id not in self.merchant_ids:
            self.merchant_ids.append(merchant.id)
            self.filter_active = True
        
    def remove_merchant(self, merchant):

        if merchant.id in self.merchant_ids:
            self.merchant_ids.remove(merchant.id)
            
            if len(self.merchant_ids) == 0 and len(self.tag_ids) == 0:
                self.filter_active = False


    def activate_filter(self):
        
        if len(self.tag_ids) > 0 or len(self.merchant_ids) > 0:
            self.filter_active = True

    def deactivate_filter(self):

        self.filter_active = False

    def clear(self):
        self.merchant_ids = []
        self.tag_ids = []

        self.deactivate_filter()