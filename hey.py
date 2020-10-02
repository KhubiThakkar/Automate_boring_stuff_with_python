# creating databases
import random
with open('text.txt','w') as f:
    name = ['ram','sita','prajakta','saif','kareena','katrina','salman','shahrukh','madhuri','pooja','anjali','lata','ramesh','riya','rocky','nikky','tina','rohan']
    last = ['arora','khan','kapoor','chopra','patel','shah','thakkar','gokhale','sinha','patil','nehra','tilak','ali']
    
    
    for i in range(30):
        r_name = random.choice(name)
        r_last = random.choice(last)
        r_email = '{}{}.falafal.com'.format(r_name,r_last)

        data = '{},{},{}\n'.format(r_name,r_last,r_email)
        f.write(data)
    