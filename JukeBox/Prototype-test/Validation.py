class InputValidation():

    @staticmethod           #this method will receive a input_value 
                            #but the min max the app will already had (0 to 5)
    def validate_integer(input_value, min_value=None, max_value=None):
        """Validates that the input is an integer within optional limits."""
        if isinstance(input_value, int):
            if (min_value is not None and input_value < min_value) or \
               (max_value is not None and input_value > max_value):
                return False, f"The input must be between {min_value} and {max_value}."
            return True, "Valid input!."
        return False, "Input is not a valid integer."
    
    @staticmethod
    def validate_float(input_value, min_value=None, max_value=None):
        """Validates that the input is a float within optional limits."""
        if isinstance(input_value, float):
            if (min_value is not None and input_value < min_value) or \
                (max_value is not None and input_value > max_value):
                    return False, f"Float must be between {min_value} and {max_value}."
            return True, "Valid float."
        return False, "Input is not a valid float." 
    
