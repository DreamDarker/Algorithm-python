import numpy as np
import matplotlib.pyplot as plt

# class of objects
class Object:
    # masses, location, acceleration and velocity 
    def __init__(self,m,x,y,a_x,a_y,v_x,v_y):
        self.m = m
        self.x = x
        self.y = y
        self.a_x = a_x
        self.a_y = a_y
        self.v_x = v_x
        self.v_y = v_y

# how universal gravitation of two objects influence obj1
def acceleration(obj1, obj2, G):
    distance_x = obj2.x - obj1.x
    distance_y = obj2.y - obj1.y
    distance = np.sqrt(distance_x**2 + distance_y**2)
    a = G * obj2.m / (distance**2)
    obj1.a_x += a * (distance_x) / distance
    obj1.a_y += a * (distance_y) / distance
    # print(G*obj1.m*obj2.m/(distance**3))

# movement of object in t
def movement(obj, dt):
    # print((obj.a_x, obj.a_y))
    obj.v_x = obj.v_x + obj.a_x * dt
    obj.v_y = obj.v_y + obj.a_y * dt
    obj.x = obj.x + obj.v_x * dt
    obj.y = obj.y + obj.v_y * dt

# movement path of earth and moon
earth_path_x = []
earth_path_y = []
moon_path_x = []
moon_path_y = []

# plot settings
plt.ion()
# 800*800
plt.figure(figsize=(8,8))

# using simulated data
# ignoring the influence of the earth and moon's gravity on the earth, otherwise the outcome could be very strange due to unreasonable parameter settings.
def fake_data():
    # initial of sun, earth and moon
    # simulated data: dt for time interval, G for gravity constant
    dt = 0.01
    G = 6.67
    sun = Object(100,0,0,0,0,0,0)
    earth = Object(10,0,10,0,0,0,0)
    moon = Object(1,0,11,0,0,0,0)

    # initial velocity of earth and moon
    earth.v_x = (G*sun.m/earth.y)**0.5
    moon.v_x = (G*earth.m/(moon.y-earth.y))**0.5 + earth.v_x

    # calculation of movements
    while(1):
        acceleration(earth, sun, G)
        # acceleration(earth, moon, G)
        acceleration(moon, sun, G)
        acceleration(moon, earth, G)
        movement(earth,dt)
        movement(moon,dt)
        earth_path_x.append(earth.x)
        earth_path_y.append(earth.y)
        moon_path_x.append(moon.x)
        moon_path_y.append(moon.y)

        #draw
        # plt.xlim((-15,15))
        # plt.ylim((-15,15))
        plt.plot(sun.x,sun.y,'or',markersize = 30)
        plt.plot(earth.x,earth.y,'ob',markersize = 6)
        plt.plot(moon.x,moon.y,'og',markersize = 2)
        plt.plot(earth_path_x,earth_path_y,'-b')
        plt.plot(moon_path_x,moon_path_y,'-g')
        plt.show()
        plt.pause(0.01)
        plt.clf()
        
        # clear acceleration
        earth.a_x = 0
        earth.a_y = 0
        moon.a_x = 0
        moon.a_y = 0

        print('distance between earth and moon:',round(np.sqrt((earth.x-moon.x)**2 + (earth.y-moon.y)**2), 2))
        
        # print('earth position:',(round(earth_path_x[-1],2),round(earth_path_y[-1],2)))
        # print('moon position:',(round(moon_path_x[-1],2),round(moon_path_y[-1],2)))


# using real data
def real_data():
    # real world data
    dt = 1 * 3600
    G = 6.6743 * (10**-11)
    sun = Object(1.99 * (10**30),0,0,0,0,0,0)
    earth = Object(5.97 * (10**24),0,1.496*(10**11),0,0,0,0)
    moon = Object(7.34 * (10**22),0,1.496*(10**11)+3.844*(10**8),0,0,0,0)

    # initial velocity of earth and moon
    earth.v_x = (G*sun.m/earth.y)**0.5
    moon.v_x = (G*earth.m/(moon.y-earth.y))**0.5 + earth.v_x
    # moon.v_x = (G*earth.m/(moon.y-earth.y))**0.5

    # calculation of movements
    while(1):
        acceleration(earth, sun, G)
        acceleration(earth, moon, G)
        acceleration(moon, sun, G)
        acceleration(moon, earth, G)
        movement(earth,dt)
        movement(moon,dt)
        earth_path_x.append(earth.x)
        earth_path_y.append(earth.y)
        moon_path_x.append(moon.x)
        moon_path_y.append(moon.y)

        # draw
        plt.xlim((-1.8*(10**11),(1.8*(10**11))))
        plt.ylim((-1.8*(10**11),(1.8*(10**11))))
        plt.plot(sun.x,sun.y,'or',markersize = 20)
        plt.plot(earth.x,earth.y,'ob',markersize = 6)
        plt.plot(moon.x,moon.y,'og',markersize = 2)
        plt.plot(earth_path_x,earth_path_y,'-b')
        plt.plot(moon_path_x,moon_path_y,'-g')
        plt.show()
        plt.pause(0.01)
        plt.clf()
        
        # clear acceleration
        earth.a_x = 0
        earth.a_y = 0
        moon.a_x = 0
        moon.a_y = 0

        print('distance between earth and moon:',round(np.sqrt((earth.x-moon.x)**2 + (earth.y-moon.y)**2), 2))
        
        # print('earth position:',(round(earth_path_x[-1],2),round(earth_path_y[-1],2)))
        # print('moon position:',(round(moon_path_x[-1],2),round(moon_path_y[-1],2)))

def main():
    print("\ndue to plot axis setting, real data may be not so intuitive")
    print("red dot corresponds to the sun, blue to the earth and green to the moon")
    print("Please choose data type: (enter 1 for real data, 2 for fake data)")
    x = input() 
    if (x == '1'):
        real_data()
    elif (x == '2'):
        fake_data()

if __name__== "__main__" :
    main()