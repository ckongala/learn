class DataObjectConverter:

    def __init__(self, config):
        self.config = config

    def convert_to_desired_format(self, data):
        """
        Taking the data and Reformating it into Data Object Format.
        """
        formatted_data = []

        native_fields = {key: data.get(key, "NONE") for key in self.config['native_fields'] if key in data}
        computed_fields = {key: data.get(key, "NONE") for key in self.config['computed_fields'] if key in data}

        data_object = {
            "media_id": self.config['media_id'],
            "media_type": self.config['media_type'],
            "media_sub_type": self.config['media_sub_type'],
            "native_fields": native_fields,
            "computed_fields": computed_fields,
        }

        formatted_data.append(data_object)

        return formatted_data