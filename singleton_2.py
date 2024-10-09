def singleton(the_class):
    instances = {}
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    return get_class

@singleton
class AppSettings:
    _instance = None

    def __init__(self):
        print("oi")
        self.tema ="O tema escuro"
        self.font = "18px"
 
@singleton        
class Teste:
    _instance = None

    def __init__(self):
        print("oi")
        

if __name__ =="__main__":
    as1  = AppSettings()
    as1.tema ="O tema claro"
    print(as1.tema)


    as2 = AppSettings()
    as2.tema ="O tema claro"
    print(as2.tema)
    
    as3 = AppSettings()
    as3.tema ="O tema claro"
    print(as3.tema)
    
    t1 = Teste()
    t2 = Teste()
    print(t1==t2)