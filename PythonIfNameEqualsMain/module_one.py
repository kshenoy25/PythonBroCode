# if __name__ == '__main__'

# checking to see:
# module can be run as a standalone program
# module can be imported  and used by other modules

# python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__

def hello():
    print("Hello")

if __name__ == '__main__':
    hello()

    #print("Running this module directly")
#else:
    #print("Running this module indirectly")