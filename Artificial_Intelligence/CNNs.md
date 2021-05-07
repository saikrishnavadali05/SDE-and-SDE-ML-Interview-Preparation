### Ideal resolution of images to feed into CNNs for training

1. Faster RCNN 
    * 800 * 600 
    * Batch Size is 1

2. For ImageNet type of networks
    * 256 * 256

3. For Smaller Networks
    * 96 * 96

4. Usual batch size is : 
    * 16 to 64 images can be fit into GPU Memory


### What is a feature Map?

1. The feature maps of a CNN capture the result of applying the filters to an input image. I.e at each layer, the feature map is the output of that layer.

2. The reason for viewing/visualizing the feature maps of the CNN is to understand, what features the CNN learnt.

### References

1. https://towardsdatascience.com/visualising-filters-and-feature-maps-for-deep-learning-d814e13bd671