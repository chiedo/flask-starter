class Serializer(object):
    __public__ = None

    def to_serializable_dict(self):
        dict = {}
        for public_key in self.__public__:
            value = getattr(self, public_key)
            if value:
                dict[public_key] = value
        return dict


def make_json(sql_alchemy_list):
    if(isinstance(sql_alchemy_list, list) is False): sql_alchemy_list = [sql_alchemy_list]
    return [i.to_serializable_dict() for i in sql_alchemy_list]
