import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { ContractService } from '../contract.service';
import { Contract } from '../contract.model';


@Component({
  selector: 'app-contracts',
  templateUrl: './contracts.component.html',
  styleUrls: ['./contracts.component.css']
})
export class ContractsComponent implements OnInit {

  listofContracts : Contract[]
  contractdetails : Contract[]
  constructor(public contractService : ContractService,public _http: HttpClient ) {}
  ngOnInit(): void {
      
    this.contractService.onSearch().subscribe( (data) =>{

      this.listofContracts = data                       });

}


detail(id){

  this.contractService.onSearch2(id).subscribe((data)  => 
   
   
  this.contractdetails = data

 
  );
}




}



