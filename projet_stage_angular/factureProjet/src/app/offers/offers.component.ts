import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Offers } from '../offers.model';
import { OffersService } from '../offers.service';

@Component({
  selector: 'app-offers',
  templateUrl: './offers.component.html',
  styleUrls: ['./offers.component.css']
})
export class OffersComponent implements OnInit {
  listofoffers : Offers[]
  offersdetails : Offers[]


  constructor(private offersService : OffersService) {}

  ngOnInit() {

  
    this.offersService.onSearch().subscribe( (data) =>{

     this.listofoffers = data });
 } 
 
 
 detail(id){

  this.offersService.onSearch2(id).subscribe((data)  => 
   
   
  this.offersdetails = data

 
  );
}

}
