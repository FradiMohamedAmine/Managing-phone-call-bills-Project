import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Bills } from '../bills.model';
import{BillService} from '../bill.service';
import { CustomerService } from '../customer.service';
import { Customer1 } from '../customer1.model';

@Component({
  selector: 'app-bills',
  templateUrl: './bills.component.html',
  styleUrls: ['./bills.component.css']
})
export class BillsComponent implements OnInit {
  notpaid: boolean;
  notcalculated: boolean;
  listofbills : Bills[]
  billdetails :Bills[]
  post_sum : any
  post_paid : any
  customer_detail : Customer1[]
  constructor(private billService : BillService,private CustomerService : CustomerService) {}

  ngOnInit(): void {
    this.billService.onSearch().subscribe( (data) =>{

      this.listofbills = data 

    } );
    


  }



  detail(id,client_id){

    this.billService.onSearch2(id).subscribe((data)  => {
    this.billdetails = data
    if(this.billdetails['paid'] == '0'){
      this.notpaid=true;
    }else this.notpaid =false ;


    if(this.billdetails['somme_tot'] == '0'){
      this.notcalculated=true;
    }else this.notcalculated =false ;
    
    this.CustomerService.onSearch2(client_id).subscribe((data)  => {
   
      this.customer_detail =data 
    }
    
    );

  }
    );}

pay (id){
  this.billService.pay_bill(id).subscribe(data =>{ 
    
    this.post_paid = data


  
  });
}

  
Calculate (id){
 this.billService.calcul_bill(id).subscribe(data =>{ 
    
    this.post_sum = data


  
  });
}



}
