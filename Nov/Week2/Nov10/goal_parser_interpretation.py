class Solution:
    def interpret(self, command: str) -> str:
        a=""
        for i in range (len(command)):
            if command[i]=="G":
                a+="G"
            elif command[i]=="(":
                if command[i+1]==")":
                    a+="o"
                else:
                    a+="al"
        return a