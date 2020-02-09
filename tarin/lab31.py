import random
  
class Agent:
    def __init__(self):
        def program(percept):abstract
        self.program=program
        
class vaccumEnvironment:

    def __init__(self):
        self.status={ loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty']),
                      loc_C:random.choice(['Clean','Dirty']),
                      loc_D:random.choice(['Clean','Dirty']),
                      }
    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action=='Right':
            if agent.location==loc_A : agent.location=loc_B
            elif agent.location==loc_C : agent.location=loc_D
        
        elif action=='Down':
            if agent.location==loc_A : agent.location=loc_C
            elif agent.location==loc_B : agent.location=loc_D
        elif action=='Left':
            if agent.location==loc_B: agent.location=loc_A
            elif agent.location==loc_D : agent.location=loc_C
        
        elif action=='Up':
            if agent.location==loc_C: agent.location=loc_A
            elif agent.location==loc_D : agent.location=loc_B
        
        elif action=='Suck':
            #if self.status[agent.location]=='Dirty'
            self.status[agent.location]='Clean'

class tableDrivenAgent(Agent):

    def __init__(self,table):
        Agent.__init__(self)
        percepts=[]

        def program(percept):
            percepts.append(percept)
            #print percepts
            action=table.get(tuple(percepts))
            print('Agent perceives %s and does %s'%(percept,action))
            return action

        self.program=program


loc_A,loc_B,loc_C,loc_D='A','B','C','D'

def tableDrivenVaccumAgent():
    table = {
              ((loc_A,'Clean'),):'Right',
              ((loc_A,'Dirty'),):'Suck',
              ((loc_B,'Clean'),):'Left',
              ((loc_B,'Dirty'),):'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
            }
    return tableDrivenAgent(table)


class reflexVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)

        action=' '

        def program(percept):

            location=percept[0]
            status=percept[1]
            
            if status=='Dirty': action= 'Suck'
            elif location==loc_A  :action= random.choice(['Right','Down'])
            elif location==loc_B :action= random.choice(['Left','Down']) 
            elif location==loc_C :action= random.choice(['Right','Up'])
            elif location==loc_D  :action= random.choice(['Left','Up'])
            percept=(location,status)
            print('Agent perceives %s and does %s'%(percept,action))

            return action
        
            
            
        self.program=program
arr=["false","false","false","false"];

class modelBasedVaccumAgent(Agent):
    
    def __init__(self):
        Agent.__init__(self)
        model={loc_A:None,loc_B:None,loc_C:None,loc_D:None}

        def program(percept):

            location=percept[0]
            status=percept[1]
            
            model[location]=status
            if model[loc_A]==model[loc_B]==model[loc_D]==model[loc_C]=='Clean': return 'NoOp'
            elif status=='Dirty': action= 'Suck'
            elif location==loc_A and arr[0]=='false':
                arr[0]='true'
                action= random.choice(['Right','Down'])
            elif location==loc_B and arr[1]=='false':
                arr[1]='true'
                action= random.choice(['Left','Down'])
            elif location==loc_C and arr[2]=='false':
                arr[2]='true'
                action= random.choice(['Right','Up'])
            elif location==loc_D and arr[3]=="false":
                arr[3]='true'
                action= random.choice(['Up','Left'])
            else: return 'noop'

            percept=(location,status)
            print('Agent perceives %s and does %s'%(percept,action))

            return action                    
            
        self.program=program

        


##
##
##Tagent=tableDrivenVaccumAgent()
##env=vaccumEnvironment()
##env.add_object(Tagent)
##for steps in range(10):
##    action=Tagent.program(env.percept(Tagent))
##    env.execute_action(Tagent,action)
##

        
##Ragent=reflexVaccumAgent()
##env=vaccumEnvironment()
##env.add_object(Ragent)
##for steps in range(25):
##    action=Ragent.program(env.percept(Ragent))
##    env.execute_action(Ragent,action)
####
##           
Magent=modelBasedVaccumAgent()
env=vaccumEnvironment()
env.add_object(Magent)
for steps in range(25):
    action=Magent.program(env.percept(Magent))
    env.execute_action(Magent,action)





