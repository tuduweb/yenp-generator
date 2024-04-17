import random

class YenpIOItem(object):
    # unique_name
    func_name: str
    func_idx : int
    io_name  : str
    pass

class YenpIOHelper(object):
    
    io_list: list

    def __init__(self) -> None:
        self.io_list = []
        self.BuildIOLists()
        print(self.io_list)
        pass

    def BuildIOLists(self):
        self._build_demo_iolists()
        pass

    def _build_demo_iolists(self):
        for idx in range(0, 15):
            io_item = YenpIOItem()
            io_item.func_idx  = random.randint(1, 3)
            io_item.func_name = "GPIO%0d" % idx
            io_item.io_name   = "IO%0d" % idx

            self.io_list.append(io_item)


class YenpRegisterItem(object):
    field_name : str
    field_range: tuple
    field_position: int
    field_reg_name: str

    def __init__(self) -> None:
        pass


class YenpRegisterHelper(object):
    field_map_list: list

    def __init__(self) -> None:
        pass

    def BuildRegisterMap(self):
        self._build_demo_register_map()
        pass

    def _build_demo_register_map(self):
        for idx in range(0, 15):
            field_item = YenpRegisterItem()
            # field_item.func_idx  = random.randint(1, 3)
            field_item.field_name = "GPIO%0d" % idx
            # field_item.io_name   = "IO%0d" % idx

            self.field_map_list.append(field_item)
        pass



class IO_SAMPLING(object):

    io_helper: YenpIOHelper

    def __init__(self) -> None:
        self.io_helper = YenpIOHelper()
        pass
    
    def BuildOneItem(self, ItemName:str):
        print("ItemName", ItemName)


if __name__ == "__main__":
    print("hellow orld")

    io_sampling = IO_SAMPLING()
    io_sampling.BuildOneItem("GPIO30")