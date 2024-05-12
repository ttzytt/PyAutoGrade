import importlib.util
import multiprocessing
from types import ModuleType
import queue

class StdIOSimulator:
    def __init__(self, simulated_module : ModuleType | str):
        self.simulated_module = simulated_module
        self.prints_to_receive_queue = multiprocessing.Queue()  # Queue to store prints to be received from the simulated module
        self.inputs_to_send_queue = multiprocessing.Queue()  # Queue to store inputs to be sent to the simulated module
        self.tested_code_ans = multiprocessing.Queue() # printed by tested code after last time they called input()

    @staticmethod
    def clear_multiprocessing_queue(q : multiprocessing.Queue):
        try:
            while True: 
                q.get_nowait()
        except queue.Empty: 
            pass


    def write_input(self, input_str):
        self.inputs_to_send_queue.put(input_str)

    def get_output(self):
        return self.prints_to_receive_queue.get()

    def output_waiting_count(self):
        return self.prints_to_receive_queue.qsize()
    def clear_output(self):
        StdIOSimulator.clear_multiprocessing_queue(self.prints_to_receive_queue)
    def input_waiting_count(self):
        return self.inputs_to_send_queue.qsize()
    def clear_input(self):
        StdIOSimulator.clear_multiprocessing_queue(self.inputs_to_send_queue)
    def tested_code_ans_count(self):
        return self.tested_code_ans.qsize()
    def clear_tested_code_ans(self):
        StdIOSimulator.clear_multiprocessing_queue(self.tested_code_ans)
    def clear_all(self):
        self.clear_output()
        self.clear_input()
        self.clear_tested_code_ans()
    def load_module(self):
        module_specs = None
        if isinstance(self.simulated_module, str): 
            # if it is a path to the module, then get its module_type now
            module_specs = importlib.util.spec_from_file_location("fake_stdio", self.simulated_module)
            self.simulated_module = importlib.util.module_from_spec(module_specs)
        elif isinstance(self.simulated_module, ModuleType):
            # if smulated_module is already module type
            module_specs = self.simulated_module.__spec__
        self.module_specs = module_specs

        exec_line = "import builtins\n" # import builtins module, so that I can define raw_input, raw_print by original input/print
        exec(exec_line, self.simulated_module.__dict__)
        # execute this line in the module's namespace/context


        def custom_print(*args, **kwargs):
            sep = kwargs.get('sep', ' ') 
            end = kwargs.get('end', '')  
            message = sep.join(map(str, args)) + end
            print("msg in custom_print: ", message)
            self.prints_to_receive_queue.put(message) 
            self.tested_code_ans.put(message)
            print("now the queue size is: ", self.output_waiting_count())

        self.simulated_module.raw_print = self.simulated_module.builtins.print
        self.simulated_module.print = custom_print

        def custom_input(prompt=None):
            self.clear_tested_code_ans()
            print("custom_input called")
            self.prints_to_receive_queue.put(prompt)
            # put the prompt into queue for the main process to receive
            return self.inputs_to_send_queue.get()

        self.simulated_module.raw_input = self.simulated_module.builtins.input
        self.simulated_module.input = custom_input

        # module_specs.loader.exec_module(self.simulated_module)
    def exec_module(self):
        self.module_specs.loader.exec_module(self.simulated_module)
    def load_and_exec_module(self):
        self.load_module()
        self.exec_module()
        
