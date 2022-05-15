pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtRegistry is ERC721Full {
    constructor() public ERC721Full("ArtRegistryToken", "ART") { }

    struct Artwork {
        string name;
        string artist;
        uint256 appraisalValue;
    }

    mapping(uint256 => Artwork) public artCollection; // TokenID => each Artwork

    // contract uses a cost-effective method of logging historical data and external appraisal reports via the Appraisal event
    event Appraisal(uint256 tokenId, uint256 appraisalValue, string reportURI);

    function registerArtwork(address owner, string memory name, string memory artist, uint256 initialAppraisalValue, string memory tokenURI) public returns (uint256) {

        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);
        artCollection[tokenId] = Artwork(name, artist, initialAppraisalValue);
        return tokenId;
    }

    function newAppraisal(uint tokenId, uint newAppraisalValue, string memory reportURI) public returns (uint256) {
        
        artCollection[tokenId].appraisalValue = newAppraisalValue;
        emit Appraisal(tokenId, newAppraisalValue, reportURI);
        return artCollection[tokenId].appraisalValue;
    }
}
