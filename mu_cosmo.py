from astropy.cosmology import FlatLambdaCDM
import argparse

cosmo = FlatLambdaCDM(H0=70, Om0=0.295)

def dist_mu(redshift):
    mu = cosmo.distmod(redshift)
    # mu = cosmo.luminosity_distance(redshift)
    return mu.value

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-z", "--z")
    args = parser.parse_args()
    redshift = float(args.z)

    dist_mu(redshift)

# import cosmolopy.distance as cd
# cosmo = {'omega_M_0':0.295, 'omega_lambda_0':0.705, 'omega_k_0':0.0, 'h':0.70}
# cosmo = cd.set_omega_k_0(cosmo)
# def dist_mu2(redshift):
#     mu = cd.luminosity_distance(redshift)
#     return mu.value