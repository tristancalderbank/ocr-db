

# may need more complex filtering in the future
class string_filter:

    filters = {"special_chars": [";", '"', "'", "(", ")"],\
               "single_quotes": ["'"]}
    
    def __init__(self, input_string):
        self.input_string = input_string
    
    def strip(self, filter_name):
        for item in self.filters[filter_name]:
            self.input_string = self.input_string.replace(item, "")

        return self.input_string

