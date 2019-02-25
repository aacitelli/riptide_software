#include "riptide_gnc/pose_edkf_interface.h"

namespace Eigen {
template<typename X, typename BinOp>
struct ScalarBinaryOpTraits<CppAD::AD<X>,X,BinOp>
{
  typedef CppAD::AD<X> ReturnType;
};

template<typename X, typename BinOp>
struct ScalarBinaryOpTraits<X,CppAD::AD<X>,BinOp>
{
  typedef CppAD::AD<X> ReturnType;
};
} // namespace Eigen

int main(int argc, char **argv)
{
    ros::init(argc, argv, "pose_edkf");
    PoseEDKFInterface poseEDKF;
    ros::spin();
}

void GetRotationYPR2Body(Ref<MatrixXf> R, float yaw, float pitch, float roll)
{
    //Matrix3f R = Matrix3f::Zero();
    float s_phi = sin(roll);
    float c_phi = cos(roll);
    float s_theta = sin(pitch);
    float c_theta = cos(pitch);
    float s_psi = sin(yaw);
    float c_psi = cos(yaw);

    R(0, 0) = c_theta * c_psi;
    R(0, 1) = c_theta * s_psi;
    R(0, 2) = -s_theta;
    R(1, 0) = s_phi * s_theta * c_psi - c_phi * s_psi;
    R(1, 1) = s_phi * s_theta * s_psi + c_phi * c_psi;
    R(1, 2) = s_phi * c_theta;
    R(2, 0) = c_phi * s_theta * c_psi + s_phi * s_psi;
    R(2, 1) = c_phi * s_theta * s_psi - s_phi * c_psi;
    R(2, 2) = c_phi * c_theta;
}

PoseEDKFInterface::PoseEDKFInterface() : nh("pose_edkf")
{
    /*int n = 2;
    int m = 3;
    vector<MatrixXi> mat;
    MatrixXi m1(n,m);
    m1.setZero();
    MatrixXi m2(m,n);
    m2.setOnes();

    mat.push_back(m1);
    mat.push_back(m2);
    cout << "m1: \n" << mat[0] << endl;
    cout << "m2: \n" << mat[1] << endl;

    Matrix3i m3 = Matrix3i::Ones();
    m1.row(0) << 1, 1, 1;
    cout << "m3: \n" << m3 << endl;
    cout << "Replaced row 1 with m3 in m1: \n" << m1 << endl;

    Matrix3Xf posIn = MatrixXf::Zero(3, 1);
    cout << "posIn \n" << posIn << endl;

    Matrix3f test = Matrix3f::Zero();
    GetRotationYPR2Body(test, 0.0, 0.0, 0.0);
    cout << "Rot: \n" << test << endl;

    copy(test);
    cout << "Mat copied: \n" << mat << endl;

    test(1,1) = 5;
    cout << "Rot: \n" << test << endl;
    cout << "Mat copied, test changed: \n" << mat << endl;

    const float var1 = 10.5;
    float var2 = var1 + 2.5;
    cout << "var2: " << endl << var2 << endl;

    int a = 5;
    stringstream ss;
    ss << "The number 'is': " << a;
    ROS_INFO("%s", ss.str().c_str());

    Vector3f v1, v2; 
    v1 << -1, -2, -3;
    v2 << 4, 5, 6;
    Vector3f v3 = v1.array() * v2.array();
    cout << "v1: " << endl << v1 << endl;
    cout << "v2: " << endl << v2 << endl;
    cout << "v1 dot v2 = " << endl << v3 << endl; */

    Matrix3f skew;
    Vector3f pqr;
    pqr << 1, 2, 3;
    skew = SkewSym(pqr);
    cout << "skew 123: " << endl << skew << endl;

    /*cout << "v1: " << endl << v1 << endl;
    v1 = v1.array().abs();
    cout << "abs of v1: " << endl << v1 << endl;

    int b = 6, m = 3, n = 4;
    try
    {
        stringstream ss;
        ss << "UpdateEKF, Dimension mismatch: Input 'Hnew' of size(" << a << ", " << b << ") does not match expected size(" << m << ", " << n << ")" << endl;
        throw std::runtime_error(ss.str());
        a = 7;
    }
    catch (exception &e)
    {
        cout << e.what();
    }
    ROS_INFO("a = %i", a);*/

    /*int a = 3;
    cout << "sgn(a) = " << Sgn(a) << endl;

    size_t n = 1, m = 2;
    vector<CppAD::AD<double>> X(n), Y(m), A(n);
    X[0] = -4.;
    CppAD::Independent(X);
    vector<double> x(n); // domain space vector
    x[0] = -2;           // argument value for derivative
    Y[0] = -Sgn(x[0]) * X[0] * X[0];
    Y[1] = X[0] * CppAD::exp(X[0]);
    CppAD::ADFun<double> f(X, Y);
    vector<double> jac(m * n);
    jac = f.Jacobian(x); // Jacobian for operation sequence
    cout << "f'(-2),1 = " << jac[0] << endl;
    cout << "f'(-2),2 = " << jac[1] << endl;

    X[0] = -4.;
    CppAD::Independent(X);
    A[0] = X[0] * X[0] * X[0]; // Declare a sub-expression, for modularity
    Y[1] = 5 * A[0] * CppAD::exp(X[0]);
    f.Dependent(X, Y);
    jac = f.Jacobian(x); // Jacobian for operation sequence
    cout << "New f'(-2),1 = " << jac[0] << endl;
    cout << "New f'(-2),2 = " << jac[1] << endl;*/

    Matrix3d id = Matrix3d::Identity();
    Matrix3d mat;
    mat << 1, 2, 3, 4, 5, 6, 7, 8, 9;
    size_t n = 6, m = 3;
    ADVectorXd X(m), Y(m), B(m);
    vector<double> x(m);
    x[0] = 1;
    x[1] = 6;
    x[2] = 20;

    CppAD::Independent(X);
    Y = X.head<3>().cross(mat * X.head<3>());
    //Y = (2*id).inverse() * B;
    CppAD::ADFun<double> f(X, Y);
    vector<double> jac(m * m);
    jac = f.Jacobian(x);
    cout << "Eigen CppAD jac[0,0] = " << jac[0] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[1] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[2] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[3] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[4] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[5] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[6] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[7] << endl;
    cout << "Eigen CppAD jac[0,0] = " << jac[8] << endl;
    
    //cout << "New f'(-2),2 = " << jac[1] << endl;
}

void PoseEDKFInterface::copy(const Ref<const MatrixXf> &m)
{
    mat = m;
}

template <typename T>
int PoseEDKFInterface::sign(T x){
    if (x > 0)
        return 1;
    else 
        return -1;
}