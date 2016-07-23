var debug = false;

var viz = {
   
   data: null, // holds data to be binded
   
   width: 850,
   height: 200,
   windowHeight: 400,
   margin: 50,
   
   svg: null, // holds svg element
   
   stats: [{"key":"pts", "label":"Points"},
           {"key":"reb", "label":"Rebounds"},
           {"key":"asts","label":"Assists"},
           {"key":"blk", "label":"Blocks"},
           {"key":"stl", "label":"Steals"},
           {"key":"fgm", "label":"FG"},
           {"key":"tpm", "label":"3FG"},
           {"key":"ftm", "label":"Free Throws"}],
    
    filters: [{"id":"Fame","label":"Hall of Fame","v":1},
              {"id":"Star","label":"All-Star","v":2}],
    
    sorters: [{"key":"years",    "label":"Years",
               "sorter":function(x,y){
                    return d3.ascending(x.career.length,y.career.length);
               }
              },
              {"key":"totals",   "label":"Total",
               "sorter":function(x,y){
                    return d3.descending(x.totals[self.state.stat],y.totals[self.state.stat]);
               }
              },
              {"key":"lastname", "label":"Name",
               "sorter":function(x,y){
                    return d3.descending(x.lastname, y.lastname);
               }
              }],
    
    stats_buttons: null,
    filter_buttons: null,
    sorter_buttons: null,
    // save state of selected options
    state: {"stat":null, "sort":null, "filter":null,
            "sorter": function() {
               if (this.sort.key == "totals") {
                  var key = this.stat.key;
                  return function(x,y) { return d3.ascending(x.totals[key],y.totals[key]);};
               }
               else return this.sort.sorter;
            },
            "selection":null
           },
    
    year_scale: null,
    tot_scale: null,
    
    players: null, // holds binded data elements
    tot_axis: null, // holds axis since it is subject to change based on selected stat
    
    linegen: null, // line generator
    
    // build menus and initialize properties and methods
    init: function() {
       var self = this;
       this.svg = d3.select("#chart");
       
       d3.select("#stats")
         .text("View: ");
         
       this.stats_buttons = d3.select("#stats")
           .selectAll("span")
           .data(this.stats)
           .enter()
           .append("span")
           .html(function(d,i) {
              var span = '<span class="button';
              if (i==0) span += ' selected';
              span += '">' + d.label +'</span>';
              if (i < self.stats.length - 1) span += ' | ';
              return span;
           });
        this.state.stat = this.stats[0]; 
        this.stats_buttons.on("click",function(d) {
          d3.select("#stats")
            .selectAll("span.button")
            .classed('selected',false);
          d3.select(this)
            .select('span')
            .classed('selected',true);
          self.state.stat = d;
          self.update();
        });
        
        d3.select("#opers")
          .append("div")
          .attr('id','filter')
          .text('Filter: ');
          
        d3.select("#opers")
          .append("div")
          .attr("id","sort")
          .text("Sort by: ");
          
        this.filter_buttons = d3.select('#filter')
            .selectAll("span")
            .data(this.filters)
            .enter()
            .append("span")
            .html(function(d,i) {
               var span = '<span class="button selected" id="' + d.id + '">' + d.label + '</span>';
               if (i < self.filters.length - 1) span += ' | ';
               return span;
            });
        this.state.filter = 3;
        this.filter_buttons.on("click",function(d) {
            if ((self.state.filter ^ d.v) == 0 || (self.state.filter ^ d.v) == 3) {
               self.state.filter = 3;
               d3.select("#filter")
                 .selectAll("span.button")
                 .classed('selected',true);
            }
            else {
               self.state.filter = self.state.filter ^ d.v;
               d3.select(this)
                 .select('span')
                 .classed('selected',false);
            }
            self.update();
        });
        
        this.sorter_buttons = d3.select('#sort')
            .selectAll("span")
            .data(this.sorters)
            .enter()
            .append("span")
            .html(function(d,i) {
              var span = '<span class="button';
              if (i==0) span += ' selected';
              span += '">' + d.label + '</span>';
              if (i < self.sorters.length - 1) span += ' | ';
              return span;
           });
        this.state.sort = this.sorters[0];
        this.sorter_buttons.on("click",function(d) {
          d3.select("#sort")
            .selectAll("span.button")
            .classed('selected',false);
          d3.select(this)
            .select('span')
            .classed('selected',true);
          self.state.sort = d;
          self.update();
        });
       
       this.draw();     
    },
    // initialize chart
    draw: function() {
       var self = this;
       this.year_scale = d3.scale.linear()
           .range([this.margin,this.width-this.margin])
           .domain([1,21]);
        
       this.tot_scale = d3.scale.linear()
           .range([this.height, this.margin])
           .domain(this.extent());
           
       var year_axis = d3.svg.axis()
           .scale(this.year_scale)
           .ticks(21);
           
       this.tot_axis = d3.svg.axis()
            .scale(this.tot_scale)
            .orient("left");
            
       this.svg.append('g')
           .attr('class','back axis')
           .attr('transform',"translate("+(this.margin+2.5*(this.data.length-1))+","+((this.data.length-1)*-3.1+this.windowHeight+this.height)+")")
           .call(year_axis);
       
       this.svg.append('g')
           .attr('class','left axis')
           .attr('transform',"translate("+(2.5*(this.data.length-1)+this.margin+this.year_scale(1))+","+((this.data.length-1)*-3.1+this.windowHeight)+")")
           .call(this.tot_axis);
       
       this.players = this.svg.selectAll("g")
           .data(this.data, function(d) { return d ? d.ilkid : this.id;})
           .enter()
           .append("g")
           .sort(this.state.sorter())
           .attr('transform', function(d,i) {
              return "translate("+(i*2.5+self.margin)+","+(i*-3.1+self.windowHeight)+")";
           })
           .classed('allstar',function(d) {
              if (d.active) return true;
              else          return false;
           })
           .classed('hof',function(d) {
              if (d.hall_of_fame) return true;
              else                return false; 
           });
       
       this.linegen = d3.svg.line()
           .interpolate('cardinal')
           .x(function(d) { return this.year_scale(d.years);})
           .y(function(d) { return this.tot_scale(d[self.state.stat.key]);});
           
       this.players.classed('player',true)
           .append('path')
           .attr('d',function(d) { return self.linegen(d.career); })
           .attr('fill','none');
           
       this.players
           .append('line')
           .classed('start',true)
           .attr('x1',this.year_scale(1))
           .attr('y1',this.tot_scale(0))
           .attr('x2',this.year_scale(1))
           .attr('y2',function(d) { return self.tot_scale(d.career[0][self.state.stat.key]);});
           
       this.players
           .append('line')
           .classed('end',true)
           .attr('x1',function(d) {
              var len = d.career.length - 1;
              return self.year_scale(d.career[len].years);
           })
           .attr('y1',this.tot_scale(0))
           .attr('x2',function(d) {
              var len = d.career.length - 1;
              return self.year_scale(d.career[len].years);
           })
           .attr('y2',function(d) {
              var len = d.career.length - 1;
              return self.tot_scale(d.career[len][self.state.stat.key]);
           });
       
       this.players
           .append('line')
           .classed('base',true)
           .attr('x1',function(d) {
              var len = d.career.length - 1;
              return self.year_scale(d.career[len].years);
           })
           .attr('y1',this.tot_scale(0))
           .attr('x2',function(d) {
              var len = d.career.length - 1;
              return self.year_scale(d.career[len].years) + 7;
           })
           .attr('y2',this.tot_scale(0));
       
       this.players
           .append('text')
           .classed('button',true)
           .attr('x',function(d) {
              var len = d.career.length - 1;
              return self.year_scale(d.career[len].years) + 10;
           })
           .attr('y',this.tot_scale(0))
           .text(function(d) { return d.firstname + " " + d.lastname; })
           .on("click",function(d) {
              if (self.state.selection == d) {
                 d3.select("#name")
                   .text("");
              
                 d3.select("#xp")
                   .text("");
              
                 d3.select("#stat")
                   .text("");
                   
                 d3.selectAll('g.player')
                   .classed('highlight',false);
                   
                 d3.select("#link")
                   .style('display','none');   
                 
                 self.state.selection = null;             
                 return;
              }
              
              self.state.selection = d;
              self.updateInfo();
           })
           .on("mouseover",function(d) {
              var datum = d;
              
              d3.select("#name")
                .text(d.firstname + " " + d.lastname + ", " + d.position);
              
              d3.select("#xp")
                .text("Experience: "  + d.career.length + " years, " + d.firstyear + "-" + d.lastyear)
              
              d3.select("#stat")
                .text(function(d) {
                   var text = "Career total: " + datum.totals[self.state.stat.key] + " " + self.state.stat.label;
                   if (self.state.stat.label.slice(-2) == "FG") text += "s made";
                   return text;
                });
              
              d3.selectAll('g.player')
                .classed('highlight',function(d) {
                   if (d == datum) return true;
                   else            return false;
                });
                 
              d3.select("#link")
                .style('display','none');
                          
           })
           .on("mouseout",function(d) {
           
              d3.select("#name")
                .text("");
              
              d3.select("#xp")
                .text("");
              
              d3.select("#stat")
                .text("");
              
              self.updateInfo();
              
              d3.selectAll('g.player')
                .classed('highlight',false);
                
              d3.selectAll('g.player')
                .classed('highlight',function(d) {
                   if (d == self.state.selection) return true;
                   else            return false;
                });
           })
       
       this.svg.append('g')
           .attr('class','front axis')
           .attr('transform',"translate("+(this.margin)+","+(this.windowHeight+this.height)+")")
           .call(year_axis);
           
       this.svg.append('text')
           .attr('class','label')
           .attr('transform',"translate("+20+","+(this.windowHeight+this.height+40)+")")
           .text("Year (in career)");
           
       this.highlight();    
    },
    // Find min/max of current stat for entire dataset
    extent: function() {
       var min = [],
           max = []; 
       var self = this;  
   
       for (i = 0;i < this.data.length; i++) {          
          min.push(d3.min(this.data[i]['career'], function(d) { return d[self.state.stat.key]; }));
          max.push(d3.max(this.data[i]['career'], function(d) { return d[self.state.stat.key]; }));
       }
       return [d3.min(min),d3.max(max)];    
    },
    // highlight top 3 Hall of Fame leaders in statistical category
    highlight: function() {
       var self = this;
       var i = 0;
       
       this.svg.selectAll('g.player')
           .sort(function(x,y) {
              return d3.descending(x.totals[self.state.stat.key],y.totals[self.state.stat.key]);
           })
           .classed('alltime', function(d) {
              var alltime = false;
              if (i < 3 && !d.active) {
                 alltime = true;
                 i += 1;
              }
              return alltime;
           });
    },
    // animate user selected options (sort, filter, statistic)
    update: function() {
       if (debug) console.log(this.state);
       this.tot_scale = d3.scale.linear()
           .range([this.height, this.margin])
           .domain(this.extent());
           
       this.tot_axis = d3.svg.axis()
            .scale(this.tot_scale)
            .orient("left");
            
       var self = this;
       
       this.svg.select('g.left')
           .transition()
           .duration(500)
           .attr('transform',"translate("+(2.5*(this.data.length-1)+this.margin+this.year_scale(1))+","+((this.data.length-1)*-3.1+this.windowHeight)+")")
           .call(this.tot_axis);
          
       this.svg.selectAll('g.player path')
           .transition()
           .duration(500)
           .attr('d',function(d) { return self.linegen(d.career);}) 
       
       this.svg.selectAll('g.player line.start')
           .transition()
           .duration(500)
           .attr('y2',function(d) { return self.tot_scale(d.career[0][self.state.stat.key]);}); 
       
       this.svg.selectAll('g.player line.end')
           .transition()
           .duration(500)
           .attr('y2',function(d) {
              var len = d.career.length - 1;
              return self.tot_scale(d.career[len][self.state.stat.key]);
           });       
            
       var plyrs = this.svg.selectAll("g.player")
          .sort(this.state.sorter())
          .classed('filter',function(d) {
              if (self.state.filter == 1 && d.active) return true;
              if (self.state.filter == 2 && !d.active) return true;
              return false;
          })
          .transition()
          .duration(5000)
          .attr('transform',function(d,i) {
             return "translate("+(i*2.5+self.margin)+","+(i*-3.1+self.windowHeight)+")";
          });
       
       if (this.state.sort.key != 'years') {
          this.svg.selectAll('g.player text')
              .transition()
              .duration(5000)
              .attr('x',this.year_scale(22));
          
          this.svg.selectAll('g.player line.base')
              .transition()
              .duration(5000)
              .attr('x2',this.year_scale(22) - 10);  
       }
       else {
          this.svg.selectAll('g.player text')
              .transition()
              .duration(5000)
              .attr('x',function(d) {
                 var len = d.career.length - 1;
                 return self.year_scale(d.career[len].years) + 10;
              });
           this.svg.selectAll('g.player line.base')
              .transition()
              .duration(5000)   
              .attr('x2',function(d) {
              var len = d.career.length - 1;
              return self.year_scale(d.career[len].years);
           })
                      
       }       
          
       this.highlight(); 
    },
    // update display with information of highlighted player
    updateInfo: function() {
       var self = this;
       var d = this.state.selection;
       
       if (d === null) return;
              
       d3.select("#name")
         .text(d.firstname + " " + d.lastname + ", " + d.position);
         
       d3.select("#xp")
         .text("Experience: "  + d.career.length + " years, " + d.firstyear + "-" + d.lastyear)
              
       d3.select("#stat")
         .text(function(e) {
           var text = "Career total: " + d.totals[self.state.stat.key] + " " + self.state.stat.label;
           if (self.state.stat.label.slice(-2) == "FG") text += "s made";
           return text;
        });
      // provide link to player's data in data source
      d3.select("#href")
        .attr('href','http://www.basketball-reference.com/players/' + d.lastname.slice(0,1).toLowerCase() + '/' + d.ilkid.toLowerCase() + '.html');
      
      d3.select('#link')
        .style('display','block');  
    }
};

d3.json('data/player_data.json',function(d) {

   viz.data = d;
   viz.init();
});