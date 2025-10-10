const ethers = require('ethers');
const { Wallet, utils } = ethers;
const { wallet1 } = require('./wallets');
const value = utils.parseUnits("1", "ether"); 
const to = "0xdD0DC6FB59E100ee4fA9900c2088053bBe14DE92";
const gasLimit = 21000;
const gasPrice = utils.parseUnits("1", "gwei"); 

const signaturePromise = wallet1.signTransaction({
    value: value,
    to: to, 
    gasLimit: gasLimit,
    gasPrice: gasPrice,
});

module.exports = signaturePromise;