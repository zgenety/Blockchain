// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity >=0.5.0 <0.9.0;

contract MyFirtsTrial {
    uint64 public FirstNumber;
    string public Operation;
    uint64 public SecondNumber;

    constructor() {
        FirstNumber = 2;
        Operation = "+";
        SecondNumber = 2;
    }

    function SetFirstNumber(uint64 Number) public {
        FirstNumber = Number;
    }

    function SetSecondNumber(uint64 Number) public {
        SecondNumber = Number;
    }

    function SetOperation(string memory oper) public {
        Operation = oper;
    }

    function Calculation() public view returns (uint128){
        if (keccak256(bytes(Operation)) == keccak256(bytes("+"))) {
            return FirstNumber + SecondNumber;
        }

        else if (keccak256(bytes(Operation)) == keccak256(bytes("-"))) {
            return FirstNumber - SecondNumber;
        }

        else if (keccak256(bytes(Operation)) == keccak256(bytes("*"))) {
            return FirstNumber * SecondNumber;
        }

        else if ((keccak256(bytes(Operation)) == keccak256(bytes("/"))) && 
                  SecondNumber != 0) {
            return FirstNumber / SecondNumber;
        }

        return 0;

}}