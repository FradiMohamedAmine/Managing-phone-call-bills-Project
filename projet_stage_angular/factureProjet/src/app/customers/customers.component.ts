import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { CustomerService } from '../customer.service';
import { Customer1 } from '../customer1.model';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-customers',
  templateUrl: './customers.component.html',
  styleUrls: ['./customers.component.css']
})
export class CustomersComponent implements OnInit {
  listOfCustomer : Customer1[]
  customerdetails : Customer1[]


  constructor( private customerService : CustomerService ) {}






  ngOnInit() {

  
     this.customerService.onSearch().subscribe( (data) =>{

      this.listOfCustomer = data 

 }
 
      );

      
    
  }



  detail(id){

    this.customerService.onSearch2(id).subscribe((data)  => 
     
     
    this.customerdetails = data
  
   
    );

  }

}