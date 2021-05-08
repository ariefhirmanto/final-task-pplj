

generateOTP = (req, res, next) => {
    var digits = '0123456789';
    let OTP = '';
    for (let i = 0; i < 4; i++ ) {
        OTP += digits[Math.floor(Math.random() * 10)];
    }
    global.OTPServer = OTP
    console.log(OTPServer);
    return res.status(200).send({ message: "OTP created!" });
 };
 
 verifyOTP = (req, res, next) => {
     let OTPClient = req.body.otp;
     if (global.OTPServer == OTPClient) {
         next();
     } else {
         res.status(401).send({ message: "Wrong OTP" });
         return;
     }
 };

const serviceOTP = {
    generateOTP,
    verifyOTP
  };
  
  module.exports = serviceOTP;