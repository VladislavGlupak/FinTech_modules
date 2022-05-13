pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtToken is ERC721Full {

    constructor() public ERC721Full("ArtToken", "ART") { }

    function registerArtwork(address owner, string memory tokenURI) public returns (uint256) {
    // TODO: add code to mint new tokens
    uint256 tokenId = totalSupply();
    _mint(owner, tokenId); // mint token
    _setTokenURI(tokenId, tokenURI); // we can call the _setTokenURI function to permanently associate the value of tokenURI with the token on the blockchain
    // the link between the token and the digital artwork
    return tokenId;
    }
}