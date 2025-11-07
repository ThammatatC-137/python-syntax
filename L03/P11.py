import math

def brunelleschi_lamp(vx, vy, x, y, height, d):
    L = math.hypot(vx - x, vy - y)
    beta = math.pi - math.atan2(vy - y, vx - x)
    H = (L - d) * math.sin(beta)
    tau = (L - d) * math.cos(beta)
    theta = math.atan2(vy - (y + height), vx - x)
    phi = math.pi - theta
    h_prime = H - tau * math.tan(phi)
    
    return L, beta, H, tau, phi, h_prime

if __name__ == '__main__':
    # Test Case 1
    vx1, vy1, x1, y1, h1, d1 = 0, 75, 100, -100, 40, 0
    L1, beta1, H1, tau1, phi1, h_prime1 = brunelleschi_lamp(vx1, vy1, x1, y1, h1, d1)
    print("Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, height={:.2f}, d={:.2f}.".format(vx1, vy1, x1, y1, h1, d1))
    print("Calc: L = {:.2f}, beta = {:.2f}, H = {:.2f}, tau = {:.2f}, phi = {:.2f}, h' = {:.2f}.".format(L1, beta1, H1, tau1, phi1, h_prime1))

    # Test Case 2
    vx2, vy2, x2, y2, h2, d2 = 0, 75, 100, -100, 40, 94
    L2, beta2, H2, tau2, phi2, h_prime2 = brunelleschi_lamp(vx2, vy2, x2, y2, h2, d2)
    print("Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, height={:.2f}, d={:.2f}.".format(vx2, vy2, x2, y2, h2, d2))
    print("Calc: L = {:.2f}, beta = {:.2f}, H = {:.2f}, tau = {:.2f}, phi = {:.2f}, h' = {:.2f}.".format(L2, beta2, H2, tau2, phi2, h_prime2))

    # Test Case 3
    vx3, vy3, x3, y3, h3, d3 = 50, 100, 50, -100, 50, 100
    L3, beta3, H3, tau3, phi3, h_prime3 = brunelleschi_lamp(vx3, vy3, x3, y3, h3, d3)
    print("Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, height={:.2f}, d={:.2f}.".format(vx3, vy3, x3, y3, h3, d3))
    print("Calc: L = {:.2f}, beta = {:.2f}, H = {:.2f}, tau = {:.2f}, phi = {:.2f}, h' = {:.2f}.".format(L3, beta3, H3, tau3, phi3, h_prime3))

    # Test Case 4
    vx4, vy4, x4, y4, h4, d4 = 0, 75, 100, 75, 50, 200
    L4, beta4, H4, tau4, phi4, h_prime4 = brunelleschi_lamp(vx4, vy4, x4, y4, h4, d4)
    print("Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, height={:.2f}, d={:.2f}.".format(vx4, vy4, x4, y4, h4, d4))
    print("Calc: L = {:.2f}, beta = {:.2f}, H = {:.2f}, tau = {:.2f}, phi = {:.2f}, h' = {:.2f}.".format(L4, beta4, H4, tau4, phi4, h_prime4))