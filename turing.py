#
# Created by Yuuki on 13/04/2025
#
from enum import Enum
from typing import Optional

class Data(Enum):
    ON = "1"
    OFF = "0"
    SPLIT = "*"
    BLANK = "B"


class Instruction:
    __slots__ = ["expected_state", "expected_data", "new_state", "new_data", "move_back"]

    def __init__(self):
        self.expected_state: int = 0
        self.expected_data: Data = Data.BLANK
        self.new_state: int = 0
        self.new_data: Data = Data.BLANK
        self.move_back: bool = False


class TuringMachine:
    def __init__(self):
        self.tape: list[Data] = []
        self.state: int = 0
        self.head = 0
        self.instructions: list[Instruction] = []

    def __find_instruction__(self, state: int, data: Data) -> Optional[Instruction]:
        for instruction in self.instructions:
            if instruction.expected_state == state and instruction.expected_data == data:
                return instruction
        return None

    def run(self):
        while True:
            current_data = self.tape[self.head]
            instruction = self.__find_instruction__(self.state, current_data)
            if instruction is None: 
                print("No instruction found for state:", self.state, "| current data:", current_data)
                break

            self.tape[self.head] = instruction.new_data
            self.state = instruction.new_state

            if instruction.move_back: self.head -= 1
            else: self.head += 1

    def print(self):
        count = 0
        num_list = []
        for state in self.tape:
            print(state.value, end="")
            if state == Data.ON: count += 1
            else:
                if count > 0: num_list.append(count - 1)
                count = 0
        if count > 0: num_list.append(count - 1)
        print()
        print("Detected number:", " ".join(map(str, num_list)))


if __name__ == "__main__":
    machine = TuringMachine()
    with open("instructions.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#"): continue
            parts = line.split()
            if (len(parts) != 5):
                print("Metadata:", line)
                continue
            instruction = Instruction()
            instruction.expected_state = int(parts[0])
            instruction.expected_data = Data(parts[1])
            instruction.new_state = int(parts[2])
            instruction.new_data = Data(parts[3])
            instruction.move_back = parts[4] == "L"
            machine.instructions.append(instruction)

    print("Instructions loaded:", len(machine.instructions))

    with open("input.txt") as file:
        line = file.readline()
        # print(line)
        for char in line:
            if char == "1":
                machine.tape.append(Data.ON)
            elif char == "0":
                machine.tape.append(Data.OFF)
            elif char == "*":
                machine.tape.append(Data.SPLIT)
            else:
                machine.tape.append(Data.BLANK)
        machine.print()
        machine.head = line.find("1")

    machine.run()
    machine.print()
