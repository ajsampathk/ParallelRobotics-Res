function theta = CosineLaw(adj,hyp,opp)
    
    numerator = (adj^2)+(hyp^2)-(opp^2);
    denominator = (2*adj*hyp);
    ratio = numerator/denominator;
    theta = acos(ratio);
end