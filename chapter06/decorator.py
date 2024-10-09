from datetime import datetime

def add_timestamps(myfunc):
    def _add_timestamps():
        print(datetime.now())
        myfunc()
        print(datetime.now())


@add_timestamps
def hello_world():
    print("Hello world")
hello_world()


hello= add_timestamps(hello_world)

