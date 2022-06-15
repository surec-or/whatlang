import re
import random

program = open("program.what", "r")
pline = program.readlines()

l = 0

barrier = ""

ifstatement = False

newvar = []

variables = {
  "newl": f"\n"
}

for line in pline:
  l += 1

  if l == 1:
    if line[0:9] == "WHAT:VDis":
      reference = line[9]
  def executecode():

    global ifstatement
    
    if ifstatement == False:
      
      newvar = []
    
      if line[0:2] == "*.":
        for c in line:
          if c == "<":
            break
          else:
            if c == "*":
              pass
            else:
              if c == ".":
                pass
              else:
                newvar.append(c)
        var = re.search("<(.*)>", line)
        variables[barrier.join(newvar)] = str(var.group(1))
    
      if line[0:2] == "#.":
        for c in line:
          if c == "<":
            break
          else:
            if c == "#":
              pass
            else:
              if c == ".":
                pass
              else:
                newvar.append(c)
        var = re.search("<(.*)>", line)
        variables[barrier.join(newvar)] = int(var.group(1))
    
      if line[0:2] == "I.":
        for c in line:
          if c == "<":
            break
          else:
            if c == "I":
              pass
            else:
              if c == ".":
                pass
              else:  
                newvar.append(c)
        var = re.search("<(.*)>", line)
        varinput = str(input(var.group(1)))
        variables[barrier.join(newvar)] = varinput

      if line[0:2] == "P.":
        
        prnt = re.search("<(.*)>", line)

        if prnt.group(1)[0] == reference:
          actprnt = variables.get(prnt.group(1)[1:])
        else:
          actprnt = prnt.group(1)
        
        print(actprnt)

      if line[0:2] == "R.":
        for c in line:
          if c == ";":
            break
          else:
            if c == "R":
              pass
            else:
              if c == ".":
                pass
              else:
                  newvar.append(c)
        
        rand1 = re.search(";(.*);", line)
        rand2 = re.search("<(.*)>", line)

        variables[barrier.join(newvar)] = str(random.randint(int(rand1.group(1)), int(rand2.group(1))))

    else:
      return


  # If statements - Actual worst thing I have ever made. Holy shit
  if line[0:3] == "IF-":   
    if line[3] == "=" or line[3] == "!":
      arg1 = re.search(";(.*);", line)
      arg2 = re.search("<(.*)>", line)
      if line[3] == "=":
        if arg1.group(1)[0] == reference:          
          if arg2.group(1)[0] == reference:
            if variables.get(arg1.group(1)[1:]) == variables.get(arg2.group(1)[1:]):
              ifstatement = False
            else:
              ifstatement = True
          else:
            if variables.get(arg1.group(1)[1:]) == arg2.group(1):
              ifstatement = False
            else:
              ifstatement = True
        else:
          if arg2.group(1)[0] == reference:
            if arg1.group(1) == variables.get(arg2.group(1)[1:]):
              ifstatement = False
            else:
              ifstatement = True
          else:
            if arg1.group(1) == arg2.group(1):
              ifstatement = False
            else:
              ifstatement = True
      else:
        if line[3] == "!":
          if arg1.group(1)[0] == reference:          
            if arg2.group(1)[0] == reference:
              if variables.get(arg1.group(1)[1:]) == variables.get(arg2.group(1)[1:]):
                ifstatement = True
              else:
                ifstatement = False
            else:
              if variables.get(arg1.group(1)[1:]) == arg2.group(1):
                ifstatement = True
              else:
                ifstatement = False
          else:
            if arg2.group(1)[0] == reference:
              if arg1.group(1) == variables.get(arg2.group(1)[1:]):
                ifstatement = True
              else:
                ifstatement = False
            else:
              if arg1.group(1) == arg2.group(1):
                ifstatement = True
              else:
                ifstatement = False
    else:
      if line[3:5] == "EL":
        if ifstatement == True:
          ifstatement = False
        else:
          ifstatement = True
      
  if line [0:3] == "IF/":
        ifstatement = False       

  
  
  else:
    if ifstatement == False:  
        executecode()

print(f"Exit code 0 with variables {variables}")