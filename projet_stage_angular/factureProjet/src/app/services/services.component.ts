import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Service } from '../service.model';
import { ServicesService } from '../services.service';


@Component({
  selector: 'app-services',
  templateUrl: './services.component.html',
  styleUrls: ['./services.component.css']
})
export class ServicesComponent implements OnInit {
  listofServices: Service[]
  servicedetails: Service[]
  constructor(private serviceService : ServicesService) {}

  ngOnInit() {

  
    this.serviceService.onSearch().subscribe( (data) =>{

     this.listofServices = data 

}

     );  }

     detail(id){

      this.serviceService.onSearch2(id).subscribe((data)  => 
       
       
      this.servicedetails = data
    
     
      );
    }

}
