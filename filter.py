

# may need more complex filtering in the future
class string_filter:


    filters = {"special_chars": [";", '"', "'", "(", ")"],\
               "single_quotes": ["'"]}
    
    def __init__(self, input_string):
        self.input_string = input_string
        self.filtered_string = self.input_string
    
    def strip(self, filter_name):
        for item in self.filters[filter_name]:
            self.filtered_string = self.filtered_string.replace(item, "")

    def remove_excess_whitespace(self):
            self.filtered_string = ' '.join(self.filtered_string.split())
        


