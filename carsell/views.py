from django.shortcuts import redirect, render
import pandas as pd
import pickle


def car_price(request):
    result = 0
    if request.method == 'POST':
        name = request.POST['Name']
        year = request.POST['year']
        km = request.POST['km']
        fuel = request.POST['fuel']
        dealer = request.POST['dealer']
        trans = request.POST['trans']
        seats = request.POST['seats']
        rpm = request.POST['rpm']
        mil = request.POST['mil']
        eng = request.POST['eng']
        power = request.POST['power']
        owner = request.POST['owner']
    
        if name != "":
            df = pd.DataFrame(columns= ['year','km_driven',	'fuel','seller_type',
                                        'transmission','mileage','engine','max_power',
                                        'seats','torque_rpm','First Owner','Fourth & Above Owner',
                                        'Second Owner','Test Drive Car','Third Owner'])
            Ownership = keychanger(owner)
            df2 = {'year':int(year),'km_driven':float(km),'fuel':float(fuel),'seller_type':int(dealer),
                   'transmission':int(trans),'mileage':float(mil),'engine':float(eng),'max_power':float(power),
                   'seats':int(seats),'torque_rpm':float(rpm),'First Owner':Ownership[0],'Fourth & Above Owner':Ownership[1],
                   'Second Owner': Ownership[2],'Test Drive Car':Ownership[3],'Third Owner':Ownership[4]}
            
            df = df.append(df2, ignore_index= True)
            filename = 'carsell\carselling_model.pickle'
            load_model = pickle.load(open(filename, 'rb'))
            result = load_model.predict(df)
            print(result)
        else:
            return redirect('homepage')
    else:
        pass
    
    return render(request, 'index.html', {'result': result}) 



def keychanger(x):
    if x == '1':
        return [1,0,0,0,0]
    elif x == '2':
        return [0,0,1,0,0]
    elif x == '3':
        return [0,0,0,0,1]
    if x =='4':
        return [0,1,0,0,0]
    if x == '5':
        return [0,0,0,1,0]