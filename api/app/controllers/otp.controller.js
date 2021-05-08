exports.generateOTP = (res) => {
    return res.status(200).send({
        message: "OTP created!"
    })
}