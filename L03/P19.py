
def time_int(event_period, viewing_speed, view_period):
  
    total_frames = viewing_speed * view_period
    
    event_period_minutes = event_period * 60
    
    shooting_interval = event_period_minutes / total_frames
    
    return shooting_interval

if __name__ == '__main__':
    T = 72   
    f = 50   
    P = 10   
    
    tau = time_int(T, f, P)
    
    print(tau, 'minutes')