const { utils, providers, Wallet } = require('ethers');
const { ganacheProvider } = require('./config');
const provider = new providers.Web3Provider(ganacheProvider);

async function donate(privateKey, charities) {
    const wallet = new Wallet(privateKey, provider);
    for (let i = 0; i < charities.length; i++) {
        const charity = charities[i];
        await wallet.sendTransaction({
            to: charity, 
            value: utils.parseEther("1.0"),
        });
    }
    return Promise.resolve();
}

module.exports = donate;