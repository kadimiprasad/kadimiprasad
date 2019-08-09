class Eval:
    def __init__(self):
        print "**Evaluate**"
    def eval_loop(self):
        Solution = ''
        while True:
            Input = raw_input("Enter the input")
            if Input.lower() == 'done':
                break
            Solution = eval(Input)
            print "Solution for Expression", Solution
obj = Eval()
obj.eval_loop()


