class ViewFilter:

    def __init__(self):

        self.tag_ids = []
        self.tags = []
        self.merchant_ids = []
        self.merchants = []
        self.filter_active = False

    def add_tag(self, tag):

        if tag.id not in self.tag_ids:
            self.tag_ids.append(tag.id)
            self.tags.append(tag)
            self.filter_active = True
        
    def remove_tag(self, tag):

        if tag.id in self.tag_ids:
            self.tag_ids.remove(tag.id)
            
            for entry in self.tags:
                if entry.id == tag.id:
                    self.tags.remove(entry)
            
            if len(self.tag_ids) == 0 and len(self.merchant_ids) == 0:
                self.filter_active = False

    def add_merchant(self, merchant):

        if merchant.id not in self.merchant_ids:
            self.merchant_ids.append(merchant.id)
            self.merchants.append(merchant)
            self.filter_active = True
        
    def remove_merchant(self, merchant):

        if merchant.id in self.merchant_ids:
            self.merchant_ids.remove(merchant.id)

            for entry in self.merchants:
                if entry.id == merchant.id:
                    self.merchants.remove(entry)
            
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
        self.merchants = []
        self.tags = []
        self.deactivate_filter()