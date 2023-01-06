class ParkingSystem {
    int b;
    int md;
    int sm;
    public ParkingSystem(int big, int medium, int small) {
        b=big;
        md=medium;
        sm=small;
    }
    
    public boolean addCar(int carType) {
        if(carType==1){
            if(b>0){
                b--;
                return true;
            }else{
                return false;
            }
        }else if(carType==2){
            if(md>0){
                md--;
                return true;
            }else{
                return false;
            }
        }else if(carType==3){
            if(sm>0){
                sm--;
                return true;
            }else{
                return false;
            }
        }else{
            return false;
        }
        
    }
}

/**`    
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */