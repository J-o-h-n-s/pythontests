import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib.animation as animation

engine = create_engine('sqlite:///Liveprice.db')

df = pd.read_sql('ETHUSDT', engine)

def animate(i):
    data = pd.read_sql('ETHUSDT', engine)
    plt.cla()
    plt.plot(data.timestamp, data.price, color='g')
    plt.axhline(y=data.price.mean(), color='r')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('ETHUSDT')
    plt.gcf().autofmt_xdate()
    plt.tight_layout()

ani = animation.FuncAnimation(plt.gcf(), animate, 100)

plt.tight_layout
plt.show()
