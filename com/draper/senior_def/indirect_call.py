def messge(msg):
    print(msg)


# messge("Hello")
act = messge


# act("Hello")


def indirect(func, args):
    func(args)


# indirect(messge, "Hello")
# indirect(act, "Hello")

schedule = [(messge, 'Hello'), (act, 'World')]

for (func, args) in schedule:
    func(args)


def make(label):
    def send(x):
        print(label, ":", x)

    return send


act = make("Hello")
act("World")
