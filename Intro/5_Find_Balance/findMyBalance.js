const { Wallet, providers, ethers } = require('ethers');
const { ganacheProvider } = require('./config');
const provider = new providers.Web3Provider(ganacheProvider);

async function findMyBalance(privateKey) {    
    const wallet = new ethers.Wallet(privateKey, provider);
    const balance = await provider.getBalance(wallet.address);
    return ethers.BigNumber.from(balance);
}

module.exports = findMyBalance;