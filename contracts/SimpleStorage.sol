// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // This will get initialzed to 0
    uint256 favNum;
    bool favBool;

    struct People {
        uint256 favNum;
        string name;
    }
    People public person = People({favNum: 5, name: "MD"});
    People[] public people;

    mapping(string => uint256) public nameToFavNum;

    function store(uint256 _favNum) public {
        favNum = _favNum;
    }

    // pure => Just do some math, free to call
    // view => Free to call
    function retreive() public view returns (uint256) {
        return favNum;
    }

    function addPerson(string memory _name, uint256 _favNum) public {
        people.push(People({favNum: _favNum, name: _name}));
        nameToFavNum[_name] = _favNum;
    }
}
