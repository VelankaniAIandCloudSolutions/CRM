<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add note</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Body</label>
                        <div class="control">
                            <textarea class="textarea" v-model="body"></textarea>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import { toast } from 'bulma-toast'

    export default {
        name: 'AddNote',
        data() {
            return {
                name: '',
                body: ''
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const note = {
                    name: this.name,
                    body: this.body,
                    client_id: this.$route.params.id,

                    
                    
                }

                const notes = {
                    name: this.name,
                    body: this.body,
                    lead_id: this.$route.params.id

                    
                    
                }


                

                await axios
                    .post('/api/v1/notes/', note)
                    .then(response => {
                        toast({
                            message: 'The note was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push({ name: 'Client', params: { id: this.$route.params.id }})
                        
                    })

                
                    .catch(error => {
                        console.log(error)
                    })


                    await axios
                    .post('/api/v1/notess/', notes)
                    .then(response => {
                        toast({
                            message: 'The Note was Added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration:2000,
                            position:'bottom-right'
                        })

                        this.$router.push({ name: 'Lead', params: { lead_id: this.$route.params.id } })

                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }

               
            
        }
    }
</script>



<!-- <style> -->

    *{
        margin:0 ;
        padding: 0;
        box-sizing: border-box;
        font-family: 'poppins', sans-serif;
    }

    body{
        height:fit-content; 
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
       
        align-items: center; 
        padding: 10px;
        background: linear-gradient(135deg, #71b7e6, #9b59b6 ); 
    }
    .conatiner{
        max-width: 700px;
        width: 100%;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 5px 10px rgba(0,0,0,0.15);
    }
    .conatiner .title::before{
        content: "";
        position: absolute;
        left: 0;
        bottom: 0;
        height: 3px;
        width: 30px;
        border-radius: 5px;
        background: linear-gradient(135deg, #71b7e6, #9b59b6);
    }
    .content form .user-details{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        margin: 20px 0 12px 0;
    }


    .content form .user-details{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        margin: 20px 0 12px 0;
    }

   



    form .user-details .input-box{
        margin-bottom: 15px;
        width: calc(100% / 2 - 20px);
    }
    .user-details .input-box input{
  height: 45px;
  width: 100%;
  outline: none;
  font-size: 16px;
  border-radius: 5px;
  padding-left: 15px;
  border: 1px solid #ccc;
  border-bottom-width: 2px;
  transition: all 0.3s ease;
}
select {
  height: 45px;
  width: 100%;
  outline: none;
  font-size: 16px;
  border-radius: 5px;
  padding-left: 15px;
  border: 1px solid #ccc;
  border-bottom-width: 2px;
  transition: all 0.3s ease;
}
.user-details .input-box input:focus,
.user-details .input-box input:valid{
  border-color: #9b59b6;
}
 form .gender-details .gender-title{
  font-size: 20px;
  font-weight: 500;
 }
 form .category{
   display: flex;
   width: 80%;
   margin: 14px 0 ;
   justify-content: space-between;
 }
 form .category label{
   /* display: flex; */
   align-items: center;
   cursor: pointer;
 }
 form .category label .dot{
  height: 18px;
  width: 18px;
  border-radius: 50%;
  margin-right: 10px;
  background: #d9d9d9;
  border: 5px solid transparent;
  transition: all 0.3s ease;
}
 #dot-1:checked ~ .category label .one,
 #dot-2:checked ~ .category label .two,
 #dot-3:checked ~ .category label .three{
   background: #9b59b6;
   border-color: #d9d9d9;
 }
 form input[type="radio"]{
   display: none;
 }
 /* form .button{
   height: 45px;
   margin: 35px 0
 } */
 /* form .button input{
   height: 100%;
   width: 100%;
   border-radius: 5px;
   border: none;
   color: #f40707;
   font-size: 18px;
   font-weight: 500;
   letter-spacing: 1px;
   cursor: pointer;
   transition: all 0.3s ease;
   background: linear-gradient(135deg, #71b7e6, #9b59b6);
 } */
 form .button input:hover{
  transform: scale(0.99);
  background: linear-gradient(-135deg, #71b7e6, #9b59b6);
  }
 @media(max-width: 584px){
 .container{
  max-width: 100%;
}
form .user-details .input-box{
    margin-bottom: 15px;
    width: 100%;
  }
  form .category{
    width: 100%;
  }
  .content form .user-details{
    max-height: 300px;
    overflow-y: scroll;
  }
  .user-details::-webkit-scrollbar{
    width: 5px;
  }
  }
  @media(max-width: 459px){
  .container .content .category{
    flex-direction: column;
    }
}





html, body{
    background: linear-gradient(-135deg, #71b7e6, #9b59b6);
    height: 100%;
}

.options {
    width: 15px;
    height: auto;
}

.box {
    text-align: center;
    width: 90%;
    margin: auto;
}

.content {
    text-align: center;
}

.table {
    width: 90%;
    margin: auto;
}

.strike {
    text-decoration: line-through;
}



div.scrollmenu {
  /* background-color: #333; */
  overflow: auto;
  white-space: nowrap;
    }



div.scrollmenu a:hover {
  background-color: #777;
}

/* div.scrollmenu th {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px;
  text-decoration: none;
  : ;
} */

/* div.scrollmenu td {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px;
  text-decoration: none;
} */







<!-- </style> -->