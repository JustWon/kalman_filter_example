
def measurement_update(estimated_mean, estimated_var, measurement_mean, measurement_var):
    new_mean = (measurement_var * estimated_mean + estimated_var * measurement_mean) / (estimated_var + measurement_var)
    new_var = estimated_var * measurement_var/(estimated_var + measurement_var)
    return new_mean, new_var

def state_prediction(estimated_mean, estimated_var, motion_control_mean, motion_control_var):
    new_mean = estimated_mean + motion_control_mean
    new_var  = estimated_var + motion_control_var
    return new_mean, new_var

if __name__ == "__main__":

    measurements = [5, 6, 7, 9, 10]
    measurement_var = 4;

    motion_control = [1, 1, 2, 1, 1]
    motion_control_var = 2

    mu = 0;
    sig = 1000;

    for i in range(5):
        mu, sig = state_prediction(mu, sig, motion_control[i], motion_control_var)
        print("predict: [%f %f]" % (mu, sig))
        mu, sig = measurement_update(mu, sig, measurements[i], measurement_var)
        print("udpate: [%f %f]" % (mu, sig))