package De.Hpi.DesisAll.DesisMultipleKeys.LocalNode.BaselineNoOptimizer.Desis.EntryPoint;

import De.Hpi.DesisAll.DesisMultipleKeys.LocalNode.BaselineNoOptimizer.Desis.Configure.Configuration;
import De.Hpi.DesisAll.DesisMultipleKeys.LocalNode.BaselineNoOptimizer.Desis.IntermediaNode.IntermediaNode;

public class EnteryPointForIntermediaNode {
    public static void main(String[] args) {
        Configuration conf = new Configuration();
        int queryNumber = conf.queryNumber;
        if(Integer.valueOf(args[1]) != 0){
            conf.queryNumber = Integer.valueOf(args[1]);
        }

        if(Integer.valueOf(args[2]) != 0){
            conf.queryModes = Integer.valueOf(args[2]);
        }

        if(Integer.valueOf(args[3]) != 0){
            conf.GeneratorThreadNumber = Integer.valueOf(args[3]);
        }

        IntermediaNode intermediaNode = new IntermediaNode(conf, Integer.valueOf(args[0]));
    }
}
